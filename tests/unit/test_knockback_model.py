from django.conf import settings

if not settings.configured:
    settings.configure()

from django.db.models import Model as DjangoModel, fields
from unittest.case import TestCase
from knockback import Model

class KnockBackModelTests(TestCase):
    class EmptyTestModel(DjangoModel):
        class Meta:
            app_label = 'tests.unit'

    class TestModelWithPrimaryKey(DjangoModel):
        test_id = fields.AutoField(primary_key=True)

        class Meta:
            app_label = 'tests.unit'

    class TestModelWithDefaultValues(DjangoModel):
        test_id = fields.AutoField(primary_key=True)
        number = fields.IntegerField(default=1)
        string = fields.CharField(max_length=50, default="foo")

        class Meta:
            app_label = 'tests.unit'

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_not_a_django_model_instance_was_provided_a_type_error_is_raised(
            self):
        with self.assertRaisesRegexp(TypeError,
            r"^A django model type or instance was not provided. Found [a-zA-Z_]+ instance instead.$"):
            Model(object())

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_not_a_django_model_type_was_provided_a_type_error_is_raised(
            self):
        with self.assertRaisesRegexp(TypeError,
            r"^A django model type or instance was not provided. Found [a-zA-Z_]+ instance instead.$"):
            Model(object)

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_instance_was_provided_no_error_is_raised(
            self):
        Model(KnockBackModelTests.EmptyTestModel())

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_instance_then_the_model_instance_attribute_is_assigned_to_the_provided_model_instance(
            self):
        model = KnockBackModelTests.EmptyTestModel()

        sut = Model(model)

        self.assertEquals(sut.model_instance, model)

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_instance_then_the_model_attribute_is_assigned_to_the_provided_model_type(
            self):
        model = KnockBackModelTests.EmptyTestModel()

        sut = Model(model)

        self.assertEquals(sut.model, model.__class__)

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_instance_and_no_id_attribute_is_found_then_the_default_id_is_assigned_to_the_id_attribute(
            self):
        model = KnockBackModelTests.EmptyTestModel()

        sut = Model(model)

        self.assertEquals(sut.idAttribute, 'id')

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_instance_and_the_id_attribute_is_found_then_the_id_name_is_assigned_to_the_id_attribute(
            self):
        model = KnockBackModelTests.TestModelWithPrimaryKey()

        sut = Model(model)

        self.assertEquals(sut.idAttribute, 'test_id')

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_instace_then_the_default_values_for_all_fields_are_in_the_defaults_dictonary(
            self):
        model = KnockBackModelTests.TestModelWithDefaultValues()

        sut = Model(model)

        self.assertEquals(sut.defaults, {'number': 1, 'string': "foo"})

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_instance_then_the_attributes_for_all_fields_are_in_the_attributes_dictonary(
            self):
        model = KnockBackModelTests.TestModelWithDefaultValues()

        sut = Model(model)

        self.assertEquals(sut.attributes, {'test_id': None, 'number': 1, 'string': "foo"})

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_type_was_provided_no_error_is_raised(
            self):
        Model(KnockBackModelTests.EmptyTestModel)

    def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_type_then_the_model_instance_attribute_equals_none(
            self):
        model = KnockBackModelTests.EmptyTestModel

        sut = Model(model)

        self.assertIsNone(sut.model_instance)


def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_type_then_the_model_attribute_is_assigned_to_the_provided_model_type(
        self):
    model = KnockBackModelTests.EmptyTestModel

    sut = Model(model)

    self.assertEquals(sut.model, model.__class__)


def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_type_and_no_id_attribute_is_found_then_the_default_id_is_assigned_to_the_id_attribute(
        self):
    model = KnockBackModelTests.EmptyTestModel

    sut = Model(model)

    self.assertEquals(sut.idAttribute, 'id')


def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_type_and_the_id_attribute_is_found_then_the_id_name_is_assigned_to_the_id_attribute(
        self):
    model = KnockBackModelTests.TestModelWithPrimaryKey

    sut = Model(model)

    self.assertEquals(sut.idAttribute, 'test_id')


def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_type_then_the_default_values_for_all_fields_are_in_the_defaults_dictonary(
        self):
    model = KnockBackModelTests.TestModelWithDefaultValues

    sut = Model(model)

    self.assertEquals(sut.defaults, {'number': 1, 'string': "something"})


def test_that_when_instantiating_a_knockback_model_and_any_argument_that_is_a_django_model_type_then_the_attributes_dictonary_is_empty(
        self):
    model = KnockBackModelTests.TestModelWithDefaultValues()

    sut = Model(model)

    self.assertEquals(sut.attributes, {})